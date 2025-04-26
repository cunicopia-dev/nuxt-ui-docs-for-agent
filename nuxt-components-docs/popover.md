<!-- source: https://ui.nuxt.com/components/popover --> # Popover

[HoverCard](https://reka-ui.com/docs/components/hover-
card)[Popover](https://reka-
ui.com/docs/components/popover)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Popover.vue)

A non-modal dialog that floats around a trigger element.

## Usage

Use a [Button](/components/button) or any other component in the default slot
of the Popover.

Then, use the `#content` slot to add the content displayed when the Popover is
open.

    
    
    <template>
      <UPopover>
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #content>
          <Placeholder class="size-48 m-4 inline-flex" />
        </template>
      </UPopover>
    </template>
    

### Mode

Use the `mode` prop to change the mode of the Popover. Defaults to `click`.

mode

hover

    
    
    <template>
      <UPopover mode="hover">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #content>
          <Placeholder class="size-48 m-4 inline-flex" />
        </template>
      </UPopover>
    </template>
    

When using the `hover` mode, the Reka UI [`HoverCard`](https://reka-
ui.com/docs/components/hover-card) component is used instead of the
[`Popover`](https://reka-ui.com/docs/components/popover).

### Delay

When using the `hover` mode, you can use the `open-delay` and `close-delay`
props to control the delay before the Popover is opened or closed.

openDelay

closeDelay

    
    
    <template>
      <UPopover mode="hover" :open-delay="500" :close-delay="300">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #content>
          <Placeholder class="size-48 m-4 inline-flex" />
        </template>
      </UPopover>
    </template>
    

### Content

Use the `content` prop to control how the Popover content is rendered, like
its `align` or `side` for example.

content.align

center

content.side

bottom

content.sideOffset

    
    
    <template>
      <UPopover
        :content="{
          align: 'center',
          side: 'bottom',
          sideOffset: 8
        }"
      >
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #content>
          <Placeholder class="size-48 m-4 inline-flex" />
        </template>
      </UPopover>
    </template>
    

### Arrow

Use the `arrow` prop to display an arrow on the Popover.

    
    
    <template>
      <UPopover arrow>
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #content>
          <Placeholder class="size-48 m-4 inline-flex" />
        </template>
      </UPopover>
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
      <UPopover v-model:open="open">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #content>
          <Placeholder class="size-48 m-4 inline-flex" />
        </template>
      </UPopover>
    </template>
    

In this example, leveraging [`defineShortcuts`](/composables/define-
shortcuts), you can toggle the Popover by pressing `O`.

### Prevent closing

Set the `dismissible` prop to `false` to prevent the Popover from being closed
when clicking outside of it or pressing escape. A `close:prevent` event will
be emitted when the user tries to close it.

Open

    
    
    <script setup lang="ts">
    const open = ref(false)
    </script>
    
    <template>
      <UPopover v-model:open="open" :dismissible="false" :ui="{ content: 'p-4' }">
        <UButton label="Open" color="neutral" variant="subtle" />
    
        <template #content>
          <div class="flex items-center gap-4 mb-4">
            <h2 class="text-highlighted font-semibold">
              Popover non-dismissible
            </h2>
    
            <UButton color="neutral" variant="ghost" icon="i-lucide-x" @click="open = false" />
          </div>
    
          <Placeholder class="size-full min-h-48" />
        </template>
      </UPopover>
    </template>
    

### With command palette

You can use a [CommandPalette](/components/command-palette) component inside
the Popover's content.

Select labels

    
    
    <script setup lang="ts">
    const items = ref([
      {
        label: 'bug',
        value: 'bug',
        chip: {
          color: 'error' as const
        }
      },
      {
        label: 'feature',
        value: 'feature',
        chip: {
          color: 'success' as const
        }
      },
      {
        label: 'enhancement',
        value: 'enhancement',
        chip: {
          color: 'info' as const
        }
      }
    ])
    const label = ref([])
    </script>
    
    <template>
      <UPopover :content="{ side: 'right', align: 'start' }">
        <UButton
          icon="i-lucide-tag"
          label="Select labels"
          color="neutral"
          variant="subtle"
        />
    
        <template #content>
          <UCommandPalette
            v-model="label"
            multiple
            placeholder="Search labels..."
            :groups="[{ id: 'labels', items }]"
            :ui="{ input: '[&>input]:h-8 [&>input]:text-sm' }"
          />
        </template>
      </UPopover>
    </template>
    

Expand code

## API

### Props

Prop |  Default |  Type   
---|---|---  
`mode`| `'click'`| ` "click" | "hover"`The display mode of the popover.  
`content`| `{ side: 'bottom', sideOffset: 8, collisionPadding: 8 }`| `
PopoverContentProps & Partial<EmitsToProps<PopoverContentImplEmits>>`The
content of the popover.Show properties

  * `disableOutsidePointerEvents?: boolean`When `true`, hover/focus/click interactions will be disabled on elements outside the `DismissableLayer`. Users will need to click twice on outside elements to interact with them: once to close the `DismissableLayer`, and again to trigger the element.
  * `side?: "top" | "right" | "bottom" | "left"`The preferred side of the trigger to render against when open. Will be reversed when collisions occur and avoidCollisions is enabled. Defaults to `"top"`.
  * `sideOffset?: number`The distance in pixels from the trigger. Defaults to `0`.
  * `align?: "start" | "center" | "end"`The preferred alignment against the trigger. May change when collisions occur. Defaults to `"center"`.
  * `alignOffset?: number`An offset in pixels from the `start` or `end` alignment options. Defaults to `0`.
  * `avoidCollisions?: boolean`When `true`, overrides the side and align preferences to prevent collisions with boundary edges. Defaults to `true`.
  * `collisionBoundary?: Element | (Element | null)[] | null`The element used as the collision boundary. By default this is the viewport, though you can provide additional element(s) to be included in this check. Defaults to `[]`.
  * `collisionPadding?: number | Partial<Record<"top" | "right" | "bottom" | "left", number>>`The distance in pixels from the boundary edges where collision detection should occur. Accepts a number (same for all sides), or a partial padding object, for example: { top: 20, left: 20 }. Defaults to `0`.
  * `arrowPadding?: number`The padding between the arrow and the edges of the content. If your content has border-radius, this will prevent it from overflowing the corners. Defaults to `0`.
  * `sticky?: "partial" | "always"`The sticky behavior on the align axis. `partial` will keep the content in the boundary as long as the trigger is at least partially in the boundary whilst "always" will keep the content in the boundary regardless. Defaults to `"partial"`.
  * `hideWhenDetached?: boolean`Whether to hide the content when the trigger becomes fully occluded. Defaults to `false`.
  * `positionStrategy?: "fixed" | "absolute"`The type of CSS position property to use.
  * `updatePositionStrategy?: "always" | "optimized"`Strategy to update the position of the floating element on every animation frame. Defaults to `'optimized'`.
  * `disableUpdateOnLayoutShift?: boolean`Whether to disable the update position for the content when the layout shifted. Defaults to `false`.
  * `prioritizePosition?: boolean`Force content to be position within the viewport.Might overlap the reference element, which may not be desired. Defaults to `false`.
  * `reference?: ReferenceElement`The custom element or virtual element that will be set as the reference to position the floating element.If provided, it will replace the default anchor element.
  * `onEscapeKeyDown?: ((event: KeyboardEvent) => void)`
  * `onPointerDownOutside?: ((event: PointerDownOutsideEvent) => void)`
  * `onFocusOutside?: ((event: FocusOutsideEvent) => void)`
  * `onInteractOutside?: ((event: PointerDownOutsideEvent | FocusOutsideEvent) => void)`
  * `onOpenAutoFocus?: ((event: Event) => void)`
  * `onCloseAutoFocus?: ((event: Event) => void)`

  
`arrow`| `false`| `boolean | PopoverArrowProps`Display an arrow alongside the popover.  
`portal`| `true`| ` string | false | true | HTMLElement`Render the popover in a portal.  
`dismissible`| `true`| `boolean`When `false`, the popover will not close when
clicking outside or pressing escape.  
`defaultOpen`| | `boolean`The open state of the popover when it is initially rendered. Use when you do not need to control its open state.  
`open`| | `boolean`The controlled open state of the popover.  
`modal`| `false`| `boolean`The modality of the popover. When set to true,
interaction with outside elements will be disabled and only popover content
will be visible to screen readers.  
`openDelay`| `0`| ` number`The duration from when the mouse enters the trigger
until the hover card opens.  
`closeDelay`| `0`| ` number`The duration from when the mouse leaves the
trigger or content until the hover card closes.  
`ui`| | ` { content?: ClassNameValue; arrow?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{ open: boolean; }`  
`content`| `{}`  
  
### Emits

Event |  Type   
---|---  
`close:prevent`| `[]`  
`update:open`| `[value: boolean]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        popover: {
          slots: {
            content: 'bg-default shadow-lg rounded-md ring ring-default data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-popover-content-transform-origin) focus:outline-none pointer-events-auto',
            arrow: 'fill-default'
          }
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
            popover: {
              slots: {
                content: 'bg-default shadow-lg rounded-md ring ring-default data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-popover-content-transform-origin) focus:outline-none pointer-events-auto',
                arrow: 'fill-default'
              }
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
            popover: {
              slots: {
                content: 'bg-default shadow-lg rounded-md ring ring-default data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-popover-content-transform-origin) focus:outline-none pointer-events-auto',
                arrow: 'fill-default'
              }
            }
          }
        })
      ]
    })
    

Expand code

[PinInputAn input element to enter a pin.](/components/pin-input)[ProgressAn
indicator showing the progress of a task.](/components/progress)

