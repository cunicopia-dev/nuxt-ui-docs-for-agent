<!-- source: https://ui.nuxt.com/components/slideover --> # Slideover

[Dialog](https://reka-
ui.com/docs/components/dialog)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Slideover.vue)

A dialog that slides in from any side of the screen.

## Usage

Use a [Button](/components/button) or any other component in the default slot
of the Slideover.

Then, use the `#content` slot to add the content displayed when the Slideover
is open.

    
    
    <template>
      <USlideover>
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #content>
          <Placeholder class="h-full m-4" />
        </template>
      </USlideover>
    </template>
    

You can also use the `#header`, `#body` and `#footer` slots to customize the
Slideover's content.

### Title

Use the `title` prop to set the title of the Slideover's header.

title

    
    
    <template>
      <USlideover title="Slideover with title">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-full" />
        </template>
      </USlideover>
    </template>
    

### Description

Use the `description` prop to set the description of the Slideover's header.

description

    
    
    <template>
      <USlideover
        title="Slideover with description"
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
      >
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-full" />
        </template>
      </USlideover>
    </template>
    

### Close

Use the `close` prop to customize or hide the close button (with `false`
value) displayed in the Slideover's header.

You can pass any property from the [Button](/components/button) component to
customize it.

close.class

    
    
    <template>
      <USlideover
        title="Slideover with close button"
        :close="{
          color: 'primary',
          variant: 'outline',
          class: 'rounded-full'
        }"
      >
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-full" />
        </template>
      </USlideover>
    </template>
    

The close button is not displayed if the `#content` slot is used as it's a
part of the header.

### Close Icon

Use the `close-icon` prop to customize the close button
[Icon](/components/icon). Defaults to `i-lucide-x`.

closeIcon

    
    
    <template>
      <USlideover title="Slideover with close button" close-icon="i-lucide-arrow-right">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-full" />
        </template>
      </USlideover>
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.close` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.close` key.

### Side

Use the `side` prop to set the side of the screen where the Slideover will
slide in from. Defaults to `right`.

side

left

    
    
    <template>
      <USlideover side="left" title="Slideover with side">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-full min-h-48" />
        </template>
      </USlideover>
    </template>
    

### Overlay

Use the `overlay` prop to control whether the Slideover has an overlay or not.
Defaults to `true`.

overlay

false

    
    
    <template>
      <USlideover :overlay="false" title="Slideover without overlay">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-full" />
        </template>
      </USlideover>
    </template>
    

### Transition

Use the `transition` prop to control whether the Slideover is animated or not.
Defaults to `true`.

transition

false

    
    
    <template>
      <USlideover :transition="false" title="Slideover without transition">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-full" />
        </template>
      </USlideover>
    </template>
    

## Examples

### Control open state

You can control the open state by using the `default-open` prop or the
`v-model:open` directive.

Open

    
    
    <script setup lang="ts">
    const open = ref(false)
    
    defineShortcuts({
      o: () => open.value = !open.value
    })
    </script>
    
    <template>
      <USlideover v-model:open="open">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #content>
          <Placeholder class="h-full m-4" />
        </template>
      </USlideover>
    </template>
    

In this example, leveraging [`defineShortcuts`](/composables/define-
shortcuts), you can toggle the Slideover by pressing `O`.

This allows you to move the trigger outside of the Slideover or remove it
entirely.

### Prevent closing

Set the `dismissible` prop to `false` to prevent the Slideover from being
closed when clicking outside of it or pressing escape. A `close:prevent` event
will be emitted when the user tries to close it.

    
    
    <template>
      <USlideover :dismissible="false" title="Slideover non-dismissible">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-full" />
        </template>
      </USlideover>
    </template>
    

### Programmatic usage

You can use the [`useOverlay`](/composables/use-overlay) composable to open a
Slideover programatically.

Make sure to wrap your app with the [`App`](/components/app) component which
uses the
[`OverlayProvider`](https://github.com/nuxt/ui/blob/v3/src/runtime/components/OverlayProvider.vue)
component.

First, create a slideover component that will be opened programatically:

SlideoverExample.vue

    
    
    <script setup lang="ts">
    defineProps<{
      count: number
    }>()
    
    const emit = defineEmits<{ close: [boolean] }>()
    </script>
    
    <template>
      <USlideover
        :close="{ onClick: () => emit('close', false) }"
        :description="`This slideover was opened programmatically ${count} times`"
      >
        <template #body>
          <Placeholder class="h-full" />
        </template>
    
        <template #footer>
          <div class="flex gap-2">
            <UButton color="neutral" label="Dismiss" @click="emit('close', false)" />
            <UButton label="Success" @click="emit('close', true)" />
          </div>
        </template>
      </USlideover>
    </template>
    

We are emitting a `close` event when the slideover is closed or dismissed
here. You can emit any data through the `close` event, however, the event must
be emitted in order to capture the return value.

Then, use it in your app:

Open

    
    
    <script setup lang="ts">
    import { LazySlideoverExample } from '#components'
    
    const count = ref(0)
    
    const toast = useToast()
    const overlay = useOverlay()
    
    const slideover = overlay.create(LazySlideoverExample, {
      props: {
        count: count.value
      }
    })
    
    async function open() {
      const shouldIncrement = await slideover.open()
    
      if (shouldIncrement) {
        count.value++
    
        toast.add({
          title: `Success: ${shouldIncrement}`,
          color: 'success',
          id: 'slideover-success'
        })
    
        // Update the count
        slideover.patch({
          count: count.value
        })
        return
      }
    
      toast.add({
        title: `Dismissed: ${shouldIncrement}`,
        color: 'error',
        id: 'slideover-dismiss'
      })
    }
    </script>
    
    <template>
      <UButton label="Open" color="neutral" variant="subtle" @click="open" />
    </template>
    

You can close the slideover within the slideover component by emitting
`emit('close')`.

### Nested slideovers

You can nest slideovers within each other.

Open

    
    
    <script setup lang="ts">
    const first = ref(false)
    const second = ref(false)
    </script>
    
    <template>
      <USlideover v-model:open="first" title="First slideover" :ui="{ footer: 'justify-end' }">
        <UButton color="neutral" variant="subtle" label="Open" />
    
        <template #body>
          <Placeholder class="h-full" />
        </template>
    
        <template #footer>
          <UButton label="Close" color="neutral" variant="outline" @click="first = false" />
    
          <USlideover v-model:open="second" title="Second slideover" :ui="{ footer: 'justify-end' }">
            <UButton label="Open second" color="neutral" />
    
            <template #body>
              <Placeholder class="h-full" />
            </template>
    
            <template #footer>
              <UButton label="Close" color="neutral" variant="outline" @click="second = false" />
            </template>
          </USlideover>
        </template>
      </USlideover>
    </template>
    

### With footer slot

Use the `#footer` slot to add content after the Slideover's body.

Open

    
    
    <script setup lang="ts">
    const open = ref(false)
    </script>
    
    <template>
      <USlideover v-model:open="open" title="Slideover with footer" description="This is useful when you want a form in a Slideover." :ui="{ footer: 'justify-end' }">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #body>
          <Placeholder class="h-full" />
        </template>
    
        <template #footer>
          <UButton label="Cancel" color="neutral" variant="outline" @click="open = false" />
          <UButton label="Submit" color="neutral" />
        </template>
      </USlideover>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`title`| | ` string`  
`description`| | ` string`  
`content`| | ` Omit<DialogContentProps, "asChild" | "as" | "forceMount"> & Partial<EmitsToProps<DialogContentImplEmits>>`The content of the slideover.Show properties

  * `disableOutsidePointerEvents?: boolean`When `true`, hover/focus/click interactions will be disabled on elements outside the `DismissableLayer`. Users will need to click twice on outside elements to interact with them: once to close the `DismissableLayer`, and again to trigger the element.
  * `trapFocus?: boolean`When `true`, focus cannot escape the `Content` via keyboard, pointer, or a programmatic focus. Defaults to `false`.
  * `onEscapeKeyDown?: ((event: KeyboardEvent) => void)`
  * `onPointerDownOutside?: ((event: PointerDownOutsideEvent) => void)`
  * `onFocusOutside?: ((event: FocusOutsideEvent) => void)`
  * `onInteractOutside?: ((event: PointerDownOutsideEvent | FocusOutsideEvent) => void)`
  * `onOpenAutoFocus?: ((event: Event) => void)`
  * `onCloseAutoFocus?: ((event: Event) => void)`

  
`overlay`| `true`| `boolean`Render an overlay behind the slideover.  
`transition`| `true`| `boolean`Animate the slideover when opening or closing.  
`side`| `'right'`| ` "top" | "bottom" | "right" | "left"`The side of the slideover.  
`portal`| `true`| ` string | false | true | HTMLElement`Render the slideover in a portal.  
`close`| `true`| `boolean | Partial<ButtonProps>`Display a close button to dismiss the slideover. `{ size: 'md', color: 'neutral', variant: 'ghost' }`  
`closeIcon`| `appConfig.ui.icons.close`| ` string`The icon displayed in the
close button.  
`dismissible`| `true`| `boolean`When `false`, the slideover will not close
when clicking outside or pressing escape.  
`open`| | `boolean`The controlled open state of the dialog. Can be binded as `v-model:open`.  
`defaultOpen`| | `boolean`The open state of the dialog when it is initially rendered. Use when you do not need to control its open state.  
`modal`| `true`| `boolean`The modality of the dialog When set to `true`,  
interaction with outside elements will be disabled and only dialog content
will be visible to screen readers.  
`ui`| | ` { overlay?: ClassNameValue; content?: ClassNameValue; header?: ClassNameValue; wrapper?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; close?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{ open: boolean; }`  
`content`| `{}`  
`header`| `{}`  
`title`| `{}`  
`description`| `{}`  
`close`| `{ ui: { overlay: (props?: Record<string, any> | undefined) => string; content: (props?: Record<string, any> | undefined) => string; header: (props?: Record<string, any> | undefined) => string; ... 5 more ...; close: (props?: Record<...> | undefined) => string; }; }`  
`body`| `{}`  
`footer`| `{}`  
  
### Emits

Event |  Type   
---|---  
`update:open`| `[value: boolean]`  
`after:leave`| `[]`  
`close:prevent`| `[]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        slideover: {
          slots: {
            overlay: 'fixed inset-0 bg-elevated/75',
            content: 'fixed bg-default divide-y divide-default sm:ring ring-default sm:shadow-lg flex flex-col focus:outline-none',
            header: 'flex items-center gap-1.5 p-4 sm:px-6 min-h-16',
            wrapper: '',
            body: 'flex-1 overflow-y-auto p-4 sm:p-6',
            footer: 'flex items-center gap-1.5 p-4 sm:px-6',
            title: 'text-highlighted font-semibold',
            description: 'mt-1 text-muted text-sm',
            close: 'absolute top-4 end-4'
          },
          variants: {
            side: {
              top: {
                content: 'inset-x-0 top-0 max-h-full'
              },
              right: {
                content: 'right-0 inset-y-0 w-full max-w-md'
              },
              bottom: {
                content: 'inset-x-0 bottom-0 max-h-full'
              },
              left: {
                content: 'left-0 inset-y-0 w-full max-w-md'
              }
            },
            transition: {
              true: {
                overlay: 'data-[state=open]:animate-[fade-in_200ms_ease-out] data-[state=closed]:animate-[fade-out_200ms_ease-in]'
              }
            }
          },
          compoundVariants: [
            {
              transition: true,
              side: 'top',
              class: {
                content: 'data-[state=open]:animate-[slide-in-from-top_200ms_ease-in-out] data-[state=closed]:animate-[slide-out-to-top_200ms_ease-in-out]'
              }
            },
            {
              transition: true,
              side: 'right',
              class: {
                content: 'data-[state=open]:animate-[slide-in-from-right_200ms_ease-in-out] data-[state=closed]:animate-[slide-out-to-right_200ms_ease-in-out]'
              }
            },
            {
              transition: true,
              side: 'bottom',
              class: {
                content: 'data-[state=open]:animate-[slide-in-from-bottom_200ms_ease-in-out] data-[state=closed]:animate-[slide-out-to-bottom_200ms_ease-in-out]'
              }
            },
            {
              transition: true,
              side: 'left',
              class: {
                content: 'data-[state=open]:animate-[slide-in-from-left_200ms_ease-in-out] data-[state=closed]:animate-[slide-out-to-left_200ms_ease-in-out]'
              }
            }
          ]
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            slideover: {
              slots: {
                overlay: 'fixed inset-0 bg-elevated/75',
                content: 'fixed bg-default divide-y divide-default sm:ring ring-default sm:shadow-lg flex flex-col focus:outline-none',
                header: 'flex items-center gap-1.5 p-4 sm:px-6 min-h-16',
                wrapper: '',
                body: 'flex-1 overflow-y-auto p-4 sm:p-6',
                footer: 'flex items-center gap-1.5 p-4 sm:px-6',
                title: 'text-highlighted font-semibold',
                description: 'mt-1 text-muted text-sm',
                close: 'absolute top-4 end-4'
              },
              variants: {
                side: {
                  top: {
                    content: 'inset-x-0 top-0 max-h-full'
                  },
                  right: {
                    content: 'right-0 inset-y-0 w-full max-w-md'
                  },
                  bottom: {
                    content: 'inset-x-0 bottom-0 max-h-full'
                  },
                  left: {
                    content: 'left-0 inset-y-0 w-full max-w-md'
                  }
                },
                transition: {
                  true: {
                    overlay: 'data-[state=open]:animate-[fade-in_200ms_ease-out] data-[state=closed]:animate-[fade-out_200ms_ease-in]'
                  }
                }
              },
              compoundVariants: [
                {
                  transition: true,
                  side: 'top',
                  class: {
                    content: 'data-[state=open]:animate-[slide-in-from-top_200ms_ease-in-out] data-[state=closed]:animate-[slide-out-to-top_200ms_ease-in-out]'
                  }
                },
                {
                  transition: true,
                  side: 'right',
                  class: {
                    content: 'data-[state=open]:animate-[slide-in-from-right_200ms_ease-in-out] data-[state=closed]:animate-[slide-out-to-right_200ms_ease-in-out]'
                  }
                },
                {
                  transition: true,
                  side: 'bottom',
                  class: {
                    content: 'data-[state=open]:animate-[slide-in-from-bottom_200ms_ease-in-out] data-[state=closed]:animate-[slide-out-to-bottom_200ms_ease-in-out]'
                  }
                },
                {
                  transition: true,
                  side: 'left',
                  class: {
                    content: 'data-[state=open]:animate-[slide-in-from-left_200ms_ease-in-out] data-[state=closed]:animate-[slide-out-to-left_200ms_ease-in-out]'
                  }
                }
              ]
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            slideover: {
              slots: {
                overlay: 'fixed inset-0 bg-elevated/75',
                content: 'fixed bg-default divide-y divide-default sm:ring ring-default sm:shadow-lg flex flex-col focus:outline-none',
                header: 'flex items-center gap-1.5 p-4 sm:px-6 min-h-16',
                wrapper: '',
                body: 'flex-1 overflow-y-auto p-4 sm:p-6',
                footer: 'flex items-center gap-1.5 p-4 sm:px-6',
                title: 'text-highlighted font-semibold',
                description: 'mt-1 text-muted text-sm',
                close: 'absolute top-4 end-4'
              },
              variants: {
                side: {
                  top: {
                    content: 'inset-x-0 top-0 max-h-full'
                  },
                  right: {
                    content: 'right-0 inset-y-0 w-full max-w-md'
                  },
                  bottom: {
                    content: 'inset-x-0 bottom-0 max-h-full'
                  },
                  left: {
                    content: 'left-0 inset-y-0 w-full max-w-md'
                  }
                },
                transition: {
                  true: {
                    overlay: 'data-[state=open]:animate-[fade-in_200ms_ease-out] data-[state=closed]:animate-[fade-out_200ms_ease-in]'
                  }
                }
              },
              compoundVariants: [
                {
                  transition: true,
                  side: 'top',
                  class: {
                    content: 'data-[state=open]:animate-[slide-in-from-top_200ms_ease-in-out] data-[state=closed]:animate-[slide-out-to-top_200ms_ease-in-out]'
                  }
                },
                {
                  transition: true,
                  side: 'right',
                  class: {
                    content: 'data-[state=open]:animate-[slide-in-from-right_200ms_ease-in-out] data-[state=closed]:animate-[slide-out-to-right_200ms_ease-in-out]'
                  }
                },
                {
                  transition: true,
                  side: 'bottom',
                  class: {
                    content: 'data-[state=open]:animate-[slide-in-from-bottom_200ms_ease-in-out] data-[state=closed]:animate-[slide-out-to-bottom_200ms_ease-in-out]'
                  }
                },
                {
                  transition: true,
                  side: 'left',
                  class: {
                    content: 'data-[state=open]:animate-[slide-in-from-left_200ms_ease-in-out] data-[state=closed]:animate-[slide-out-to-left_200ms_ease-in-out]'
                  }
                }
              ]
            }
          }
        })
      ]
    })
    

Expand code

[SkeletonA placeholder to show while content is
loading.](/components/skeleton)[SliderAn input to select a numeric value
within a range.](/components/slider)

